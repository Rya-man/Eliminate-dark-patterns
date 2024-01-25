// change the code for specific site

// Function to find and highlight sponsored posts
async function findAndHighlightSponsored() {
    // Get the active tab
    let [tab] = await chrome.tabs.query({ active: true, currentWindow: true });

    // Execute script in the active tab
    chrome.scripting.executeScript({
        target: { tabId: tab.id },
        func: () => {
            // Get all elements with the class "a-section a-spacing-base"
            let frames = document.body.getElementsByClassName("a-section a-spacing-base");

            // Loop through each frame
            for (let i = 0; i < frames.length; i++) {
                // Check if the frame contains elements with the class "puis-label-popover-default"
                if (frames[i].getElementsByClassName("puis-label-popover-default").length > 0) {
                    // If found, highlight the entire frame
                    frames[i].style.backgroundColor = "red";
                }
            }
        }
    });
}

async function remove_money() {
    // Get the active tab
    let [tab] = await chrome.tabs.query({ active: true, currentWindow: true });

    // Execute script in the active tab
    chrome.scripting.executeScript({
        target: { tabId: tab.id },
        func: () => {
            // Get all elements with the class "a-section a-spacing-base"
            let frames = document.body.getElementsByClassName("a-row");

            // Loop through each frame
            for (let i = 0; i < frames.length; i++) {
                // Check if the frame contains elements with the class "puis-label-popover-default"
                if (frames[i].getElementsByClassName("a-price-whole").length > 0) {
                    // If found, highlight the entire frame
                    frames[i].remove()
                }
            }
        }
    });
}

// Function to fetch site URL and pass it to an API
async function fetchSiteUrlAndPassToApi() {
    // Get the active tab
    let [tab] = await chrome.tabs.query({ active: true, currentWindow: true });

    // Get the URL of the active tab
    let siteUrl = tab.url;

    // Replace the placeholder API_URL with your actual API endpoint
    let apiUrl = 'https://53b3-106-51-8-242.ngrok-free.app';

    // Perform the API request with the site URL
    /*fetch(apiUrl+"/"+siteUrl , {
        method: 'POST',
    })*/
    chrome.tabs.create({ url: apiUrl+"/"+siteUrl });

}

async function remove_reviews() {
    // Get the active tab
    let [tab] = await chrome.tabs.query({ active: true, currentWindow: true });

    // Execute script in the active tab
    chrome.scripting.executeScript({
        target: { tabId: tab.id },
        func: () => {
            // Get all elements with the class "a-section a-spacing-base"
            let frames = document.body.getElementsByClassName("a-declarative");

            // Loop through each frame
            for (let i = 0; i < frames.length; i++) {
                
                    // If found, highlight the entire frame
                    frames[i].remove()
                
            }
        }
    });
}
// Add event listeners to the buttons
document.getElementById("findSponsored").addEventListener("click", findAndHighlightSponsored);
document.getElementById("fetchSiteUrl").addEventListener("click", fetchSiteUrlAndPassToApi);
document.getElementById("remove_money").addEventListener("click", remove_money);
document.getElementById("remove_reviews").addEventListener("click", remove_reviews);

