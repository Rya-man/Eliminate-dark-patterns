//amazon.js

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

//function to remove prices
async function remove_money() {
    // Get the active tab
    let [tab] = await chrome.tabs.query({ active: true, currentWindow: true })
    // Execute script in the active tab
    chrome.scripting.executeScript({
        target: { tabId: tab.id },
        func: () => {
            let frames = document.body.getElementsByClassName("a-row");
            // Loop through each frame
            for (let i = 0; i < frames.length; i++) {
                if (frames[i].getElementsByClassName("a-price-whole").length > 0) {
                    frames[i].remove() //remove prices
                }
            }
        }
    });
}

// Function to fetch site URL and pass it to API
async function fetchSiteUrlAndPassToApi() {
    try {
        // Get the active tab
        let [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
        // Get the URL of the active tab
        let siteUrl = tab.url;
        // Replace the placeholder API_URL with your actual API endpoint
        let apiUrl = 'API_URL';
        // Perform the API request with the site URL
        let response = await fetch(apiUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ url: siteUrl }), // Send the site URL in the request body
        });
        let responseData = await response.json();
        // Open a new tab with the URL received from the API
        chrome.tabs.create({ url: responseData.newUrl });
    } 
}

//function to load search engine
async function SecrchEngine() {
    try {
        // Get the active tab
        let [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
        // Replace the placeholder API_URL with your actual API endpoint
        let apiUrl = 'API_URL';
        let response = await fetch(apiUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ url: "/search-engine" }), // Send the request body
        });
        let responseData = await response.json();
        // Open a new tab with the URL received from the API
        chrome.tabs.create({ url: responseData.newUrl });
    } 
}

//function to remove reviews
async function remove_reviews() {
    // Get the active tab
    let [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
    // Execute script in the active tab
    chrome.scripting.executeScript({
        target: { tabId: tab.id },
        func: () => {
            let frames = document.body.getElementsByClassName("a-declarative");
            // Loop through each frame
            for (let i = 0; i < frames.length; i++) {
                    frames[i].remove()   // remove review
            }
        }
    });
}

// Add event listeners to the buttons
document.getElementById("findSponsored").addEventListener("click", findAndHighlightSponsored);
document.getElementById("fetchSiteUrl").addEventListener("click", fetchSiteUrlAndPassToApi);
document.getElementById("remove_money").addEventListener("click", remove_money);
document.getElementById("remove_reviews").addEventListener("click", remove_reviews);
document.getElementById("serachEngine").addEventListener("click", SecrchEngine);
