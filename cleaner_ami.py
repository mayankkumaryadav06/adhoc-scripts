"""
Have commented out code for cleaning ami at the bottom. Uncomment to delete ami
"""
import argparse
from datetime import datetime, timedelta
import time
import boto3
from botocore.exceptions import ClientError

intervals = (
    #('weeks', 604800),  # 60 * 60 * 24 * 7
    ('days', 86400),    # 60 * 60 * 24
    ('hours', 3600),    # 60 * 60
    ('minutes', 60),
    ('seconds', 1),
    )

def display_time(seconds, granularity=2):
    result = []

    for name, count in intervals:
        value = seconds // count
        if value:
            seconds -= value * count
            if value == 1:
                name = name.rstrip('s')
            result.append("{} {}".format(value, name))
    return ', '.join(result[:granularity])

def main () :
# Parse the project name
        parser = argparse.ArgumentParser()
        parser.add_argument(
                '--days', default=30, type=int,
                help='Clean up AMI images older than X days (default = 30 days)',
        )
        parser.add_argument(
                '--region', default='eu-west-2', type=str,
                help='AWS region to watch for AMIs (default = us-west-2)',
        )
        parser.add_argument(
                '--owner', default='someaccountid', type=str,
                help='AWS account owner ID (default account number is fictional)',
        )

        # Get the timeout from config
        args = parser.parse_args()
        days_count = args.days
        aws_region = args.region
        account_owner_image_id = args.owner
        ami_age_limit = datetime.now() - timedelta(days=days_count)

        ec2_client = boto3.client('ec2', region_name=aws_region)

        images_list = ec2_client.describe_images(Owners=[account_owner_image_id])
        cleanup_counter = 0
        total_sum = 0

        #print (images_list)

        for image in images_list['Images']:
                image_name = image['Name']
                if image_name in 
                image_id = image['ImageId']
                date_string = image['CreationDate']
                
                current_time = datetime.now()
                current_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
                pattern = '%Y-%m-%d %H:%M:%S'
                current_epoch = int(time.mktime(time.strptime(str(current_time), pattern)))
                    
                image_dt = datetime.strptime(date_string, '%Y-%m-%dT%H:%M:%S.%fZ')
                ami_epoch_time = int(time.mktime(time.strptime(str(image_dt), pattern)))
                    
                time_difference = current_epoch - ami_epoch_time
                cost_per_sec = 0.00000000433
                cost_incurred = cost_per_sec * time_difference
                
                time_diff = display_time(time_difference)
                instances_list = ec2_client.describe_instances(
                    Filters=[{'Name': 'image-id', 'Values': [image_id]}]
                )
                active_reservations = instances_list['Reservations']
                if not active_reservations:
                    for deviceName in image['BlockDeviceMappings'] :

                        if  :
                            print('image_id[%s] image_dt[%s] Size[%s] Current Time[%s] Time Running[%s] Cost[%.10f]\n' % (image_id, image_dt, deviceName['Ebs']['VolumeSize'] , current_time, time_diff , cost_incurred))
                            total_sum = total_sum + cost_incurred
                        except:
                            pass
                        #print('image_id[%s] image_dt[%s] Size[%s] Current Time[%s]\n' % (image_id, image_dt, deviceName['Ebs']['VolumeSize'] , current_time))
                        
        print ("total_sum: [%s]" % total_sum)        
                # image_name = image['Name']
                
                
                # if image_dt > ami_age_limit:
                        # instances_list = ec2_client.describe_instances(
                                # Filters=[{'Name': 'image-id', 'Values': [image_id]}]
                        # )
                        # active_reservations = instances_list['Reservations']
                        # if not active_reservations:
                        # # try:
                            # # ec2_client.deregister_image(ImageId=image_id)
                        # # except ClientError:
                            # # pass
                        # #print

                                # print('Image [%s] [%s] has to be removed\n' % (image_name, image_dt))
                                # cleanup_counter += 1

        # if cleanup_counter:
                # print('Totally %s images have been cleaned up.' % cleanup_counter)
        # else:
                # print('There is no images to be removed.')

if __name__ == "__main__":
        main()


