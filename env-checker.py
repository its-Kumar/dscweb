import os

if 'ENVIRONMENT_NAME' in os.environ:
    print("Environment set")
    print("ENVIRONMENT_NAME ", os.environ['ENVIRONMENT_NAME'])
else:
    print("Environment variable not set")
