# RCB Ticket Notifier

This repository contains a script that scrapes the Royal Challengers Bangalore (RCB) website every minute to check for available tickets. The script is scheduled to run every minute using a cron job to ensure real-time monitoring of ticket availability.

## Overview

The purpose of this script is to provide timely updates on the availability of tickets for Royal Challengers Bangalore matches. By running every minute, it ensures that you have the most current information on ticket sales, allowing you to act quickly when tickets become available.

## How It Works

The script performs the following tasks:

1. **Fetches the RCB website content:**
    - The script makes an HTTP request to the RCB tickets webpage to retrieve the latest content.
    
2. **Parses the website content:**
    - It uses an HTML parsing library, such as BeautifulSoup, to process the retrieved HTML and locate the section of the webpage that lists ticket availability.

3. **Checks for ticket availability:**
    - The script searches for specific indicators within the parsed HTML that signify whether tickets are available or not.

4. **Notifies the user:**
    - If tickets are found to be available, the script sends a notification to the user. This can be configured to send an **email** and a message via **telegram bot**.


## Usage

Once the script is set up and the cron job is configured, it will run automatically every minute. You can monitor its activity through the generated logs or by the notifications it sends when tickets become available.

