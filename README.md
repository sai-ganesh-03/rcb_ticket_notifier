# RCB Ticket Notifier

## Overview

This repository contains a script that utilizes Selenium to scrape the Royal Challengers Bangalore (RCB) website every minute, checking for available tickets. The script is scheduled to run every minute using a cron job, ensuring real-time monitoring of ticket availability.

The purpose of this script is to provide timely updates on the availability of tickets for Royal Challengers Bangalore matches. By running every minute, it ensures that you have the most current information on ticket sales, enabling you to act quickly when tickets become available.

## How It Works

The script performs the following tasks:

1. **Fetches the RCB website content:**
    - The script uses Selenium to navigate to the RCB tickets webpage, allowing it to interact with dynamic content.
    
2. **Parses the website content:**
    - It locates the section of the webpage that lists ticket availability by inspecting the HTML structure.
    
3. **Checks for ticket availability:**
    - The script searches for specific indicators within the webpage content that signify whether tickets are available or not.

4. **Notifies the user:**
    - If tickets are found to be available, the script sends a notification to the user. This can be configured to send an **email** and a message via **Telegram bot**.

## Usage

Once the script is set up and the cron job is configured, it will run automatically every minute. You can monitor its activity through the generated logs or by the notifications it sends when tickets become available.
