const copyButton = document.querySelector("[data-copy-results]");
const resultsList = document.querySelector("#results-list");

if (copyButton && resultsList) {
    copyButton.addEventListener("click", async () => {
        const titles = Array.from(resultsList.querySelectorAll("li"))
            .map((item, index) => `${index + 1}. ${item.textContent.trim()}`)
            .join("\n");

        try {
            await navigator.clipboard.writeText(titles);
            copyButton.textContent = "Copied";
            window.setTimeout(() => {
                copyButton.textContent = "Copy all";
            }, 1600);
        } catch (error) {
            copyButton.textContent = "Copy failed";
            window.setTimeout(() => {
                copyButton.textContent = "Copy all";
            }, 1600);
        }
    });
}
