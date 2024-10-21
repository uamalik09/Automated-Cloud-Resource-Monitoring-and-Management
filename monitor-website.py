import boto3
import requests
import smtplib
import os
import paramiko
import time
import schedule

# Environment variables for email credentials and AWS configuration
EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
AWS_REGION = os.environ.get('AWS_REGION', 'eu-west-3')  
INSTANCE_ID = os.environ.get('INSTANCE_ID')  
KEY_FILE_PATH = os.environ.get('KEY_FILE_PATH')  


ec2_client = boto3.client('ec2', region_name=AWS_REGION)

def restart_server_and_container():
    """Reboots the EC2 server and restarts the application container."""
    print('Rebooting the EC2 server...')
    
    # Reboot the EC2 instance
    ec2_client.reboot_instances(InstanceIds=[INSTANCE_ID])
    
    # Wait until the EC2 instance is running again
    ec2_client.get_waiter('instance_running').wait(InstanceIds=[INSTANCE_ID])
    
    # Once the server is running, restart the container
    time.sleep(5)
    restart_container()


def send_notification(email_msg):
    """Sends an email notification in case of application failure."""
    print('Sending an email...')
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.ehlo()
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        message = f"Subject: SITE DOWN\n{email_msg}"
        smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, message)


def restart_container():
    """Restarts the Docker container on the EC2 instance via SSH."""
    print('Restarting the Docker container on EC2 instance...')
    
    # Connect to EC2 instance via SSH
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname='<EC2_PUBLIC_IP>', username='ec2-user', key_filename=KEY_FILE_PATH)
    
    # Restart the Docker container
    stdin, stdout, stderr = ssh.exec_command('docker start ee6b82b80ecd')
    print(stdout.readlines())
    ssh.close()


def monitor_application():
    """Monitors the application running on the EC2 instance."""
    try:
        response = requests.get('http://<EC2_PUBLIC_IP>:8080/')  # Replace with your EC2 public IP and app port
        if response.status_code == 200:
            print('Application is running successfully!')
        else:
            print('Application Down. Fix it!')
            msg = f'Application returned {response.status_code}'
            send_notification(msg)
            restart_container()
    except Exception as ex:
        print(f'Connection error happened: {ex}')
        msg = 'Application not accessible at all'
        send_notification(msg)
        restart_server_and_container()



schedule.every(5).minutes.do(monitor_application)


while True:
    schedule.run_pending()
