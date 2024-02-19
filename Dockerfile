# Use the official Odoo 17 image as the base
FROM odoo:17

# Set the working directory to /mnt/extra-addons, which is one of the default addons paths for Odoo
WORKDIR /mnt/extra-addons

# Copy your custom addons from the custom-addons directory into the container
COPY custom-addons/ .

# The base image odoo:17 already sets the correct entrypoint and CMD, so Odoo will start automatically
# when the container is run, and it will automatically include modules in /mnt/extra-addons
