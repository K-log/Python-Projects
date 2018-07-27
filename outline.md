Application Initialization:
    import BeautifulSoup
    Declare a string variable current_speed
    Declare a string variable remote_host

Application Start:
    Try 
        Request the webpage contents from the server of the URL stored in server_URL
    Except
        No response from server with the given URL
        Retry again in 5 minutes

    If we have the contents of the webpage
        Iterate through the html divs to find the correct div
        Iterate throguh the contents of the div to find the data
        Set the value of current_speed to be what is stored in the html
    else
        repeat from the top

Application Exit:
