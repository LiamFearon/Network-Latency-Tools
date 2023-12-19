# Network Latency Tools

With the tools provided, you can parse and visualize the results of a recursive ping command to your desired address. This can be used for both local and external addresses, noting the time taken for the ping to complete. This measurement can be useful for troubleshooting connectivity issues with your network or website, as you can understand the consistency of the connection and spot if there is variance to any degree.


# How to use

These tools are part of a process that must be undergone to achieve the end goal of viewing your network performance in a graphical format

## 1. Run your ping command

To gather the data needed to measure performance, we will first use the classic ping command in Windows CMD. This command will send a packet of data to the specified address and await a response before confirming a successful ping has occurred.  Its from the resulting values of this command (Specifically; time) that we will be able to measure the variance of the connection.

If your looking to measure your WAN performance, this can be done by pinging googles DNS Server @8.8.8.8. The command you would use for this looks like so:

    ping -t 8.8.8.8 >> ping_results.txt
If however, you're looking to test your LAN performance, you can instead ping your router. Your router's IP address is depending on your configuration, so you will need to find your specific IP to use. However your command should look something like the following:

    ping -t 192.168.0.1 >> ping_results.txt
Run either of the above commands for as long as you would like your testing to take place. Once you've gathered enough data, press Ctrl+C to terminate the command. We will find our results in a file named 'ping_results.txt' in the folder where our command was ran. 

## 2. Parse your results

This is where the 2 files provided come into play. As we now have our data in a text file, we will need to extract the specific data we're looking for and move it into a more friendly format. To so this we will run `ParseResults.py`. This file will sort through our 'ping_results.txt' and gather the times of all requests, outputting said findings into a .csv file, for reasons we will see in the next stage.

With our parsing of the results now done, we can see the fruits of our labor by running `ShowResults.py`. If the above stages have been completed correctly, you should be looking at a graph of ping time against ping number. Thanks for following this guide and best of luck with your networking issues!

## 3. FAQs

> My chart is empty 😱

This will be the case where `ParseResults.py` is not finding our file 'ping_results.txt'. To solve this, simply copy the your results file into the same folder that you have `ParseResults.py` or update the file path within the python file.

> Something about missing MatPlotLib or Pandas

Missing dependencies is a quick fix by running the following PIP commands:

    pip install matplotlib
    pip install pandas

> I don't know what to do with any of this

Sounds like you're not too familiar with Python, no worries! Simply download Python through the Windows App Store and run the above pip install commands to have everything you need. When ready, just run the files provided typing (or copying) the following into your CMD window

> How do I reach these python files?

To find and run these files, you have 2 options. Navigate CMD to the directory where you have saved the files, or move said files to where your CMD opens by default. For simplicity, I'd suggest moving the files provided to your user folder as this is the default starting location for CMD and will look something like the following:

    C:\Users\[Your Username]


