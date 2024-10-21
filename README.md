# Automated Cloud Resource Monitoring and Management

This project automates the monitoring and management of cloud resources such as Amazon EC2 instances and EKS clusters. It is designed to run continuous checks, perform maintenance tasks, and send notifications in case of issues. This project leverages AWS Boto3 and other tools to ensure that cloud environments are monitored effectively and issues are handled automatically.

## Features

### 1. **EC2 Instance Status Monitoring**

- **Periodic Status Check**: Automatically checks the status of all EC2 instances in a specified region every 5 seconds.
- **Real-time Feedback**: Provides details about each instance’s state (e.g., running, stopped), system health, and instance health.
- **Customizable**: Can be configured to run on any AWS region, making it adaptable to different deployment scenarios.

### 2. **EKS Cluster Information Retrieval**

- **Cluster Overview**: Retrieves the status, endpoint, and version of all EKS clusters in a specified AWS region.
- **Scalable**: Supports multiple clusters and can handle scaling by fetching details for each cluster individually.
- **Cluster Health Visibility**: Provides real-time visibility into the operational status of Kubernetes clusters.

### 3. **Automated Snapshot Management for EC2 Volumes**

- **Snapshot Creation**: Automatically creates snapshots for EC2 volumes that are tagged with specific identifiers (e.g., "prod"). This ensures that critical data is backed up daily.
- **Resource Filtering**: Filters volumes based on specific tags, so only the required volumes are processed.
- **Daily Backups**: Scheduled to create snapshots every day, ensuring that the latest state of the volumes is preserved.

### 4. **Snapshot Cleanup for Cost Optimization**

- **Automatic Deletion of Older Snapshots**: Deletes older snapshots, keeping only the most recent ones (by default, the latest 2 snapshots are retained). This helps save on storage costs by avoiding the accumulation of unnecessary backups.
- **Date-based Sorting**: Snapshots are sorted by creation date, ensuring only the oldest ones are removed.

### 5. **Automated EC2 Instance Management**

- **Server Reboot**: Automatically reboots the EC2 instance if the application is inaccessible after attempting to restart the container.
- **Customizable for Different Servers**: Easily configurable to reboot any EC2 instance by changing the instance ID in the script.

### 6. **AWS EC2 Application Health Monitoring**

- **Periodic Application Health Check**: Continuously monitors the health of an application hosted on an AWS EC2 instance by sending requests to the server’s endpoint.
- **Automated Container Restarts**: If the application is down or non-responsive, the system automatically attempts to restart the Docker container running the application.
- **Server Reboot on Failure**: If restarting the container doesn't resolve the issue, the script reboots the EC2 instance and waits for it to be fully operational before retrying the container restart.
- **Docker Integration**: Automatically starts the appropriate Docker container once the server is back online, ensuring the application is quickly restored.

### 7. **Email Notification System**

- **Downtime Alerts**: Sends an email alert when the monitored application goes down or becomes inaccessible.
- **Detailed Error Messages**: Emails include detailed error messages explaining the reason for downtime (e.g., HTTP status codes or connection failures).
- **Continuous Monitoring**: After sending an alert, the system continues to monitor and will send additional notifications if necessary.

### 8. **Task Scheduling**

- **Automated Task Scheduling**: Uses the `schedule` library to automate the execution of tasks like EC2 status checks, snapshot creation, and server health monitoring.
- **Flexible Timing**: Allows tasks to be scheduled at any interval (e.g., every 5 seconds, every day, every 5 minutes), providing flexibility based on the use case.
- **Efficient Resource Management**: Ensures that all monitoring and management tasks run at defined intervals without overwhelming the system with constant checks.

### 9. **Error Handling and Recovery**

- **Robust Error Handling**: Built-in exception handling to deal with network issues, API rate limits, and other failures.
- **Recovery Actions**: Automatically initiates recovery actions like restarting Docker containers or rebooting servers if issues are detected.
- **Minimal Downtime**: Ensures minimal downtime by rapidly detecting failures and performing automated recovery steps.

### 10. **Customizable Cloud Resources**

- **Multi-cloud Support**: Although primarily focused on AWS, the scripts are modular and can be extended to manage other cloud services.
- **Tag-based Filtering**: For EC2 volumes and snapshots, resources can be filtered by tags, making it easy to apply these operations only to specific resources.
- **Region Configurable**: Easily change AWS region settings to monitor different geographic regions.

### 11. **Scalable Architecture**

- **Multiple Instances**: The solution supports multiple EC2 instances, volumes, and snapshots, making it scalable to large infrastructures.
- **Multi-cluster EKS Management**: Designed to handle multiple EKS clusters efficiently, making it suitable for Kubernetes environments with multiple clusters.

---

This project is built with cloud reliability and automation in mind. It reduces manual intervention in cloud resource management, ensuring that critical infrastructure is continuously monitored, managed, and recovered from failures with minimal downtime and human intervention.
