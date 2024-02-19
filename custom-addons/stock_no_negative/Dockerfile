# Use the official Odoo image as a parent image
FROM odoo:17.0

# Set the working directory in the container
WORKDIR /usr/src/odoo

# Copy the project directory contents into the container at /mnt/extra-addons
COPY stock_no_negative /mnt/extra-addons

# Set default user when running the container
USER odoo
