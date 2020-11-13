# gcp_manage_sechedule_vm_instances
Code to be used in a GCP servelles function to start or stop an vm instance 

The main function code is a template to be deployed in GCP function

The function receives a PUB/SUB message with the payload

Steps:
  1 - Create a pub/sub topic
  2 - Create a job in cloud scheduler
  3 - send the payload in cloud scheduler
