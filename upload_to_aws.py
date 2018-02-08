
import os
import glob

import boto3

from keys import aws_abel_co


def main():
    s3_resource = boto3.resource('s3', aws_access_key_id=aws_abel_co['Access key ID'],
                  aws_secret_access_key=aws_abel_co['Secret access key'],
                  region_name='us-west-2')
    s3_client = boto3.client('s3', aws_access_key_id=aws_abel_co['Access key ID'],
                aws_secret_access_key=aws_abel_co['Secret access key'],
                region_name='us-west-2')

    build_dir = '_build'
    bucket = 'practicalprojectexecution'
    for file_path in glob.glob(os.path.join(build_dir, '**'), recursive=True):
        if os.path.isfile(file_path):
            key = file_path.replace(build_dir, '')
            if key.startswith(os.sep):
                key = key[1:]
            key = key.replace(os.sep, '/')
            if not key.startswith('_sources') and not key.startswith('venv'):
                extra_args = {'ACL': "public-read"}
                if key.endswith('.html'):
                    extra_args['ContentType'] = 'text/html'
                elif key.endswith('.js'):
                    extra_args['ContentType'] = 'application/javascript'
                elif key.endswith('.css'):
                    extra_args['ContentType'] = 'text/css'
                print(file_path, key, extra_args)
                # todo: check if changed before bothering to upload
                s3_resource.meta.client.upload_file(file_path, bucket, key,
                                                    ExtraArgs=extra_args)

    print('https://s3-us-west-2.amazonaws.com/practicalprojectexecution/index.html')


if __name__ == '__main__':
    main()
