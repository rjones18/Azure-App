function toggleSource(event, sourceId) {
    event.preventDefault();

    const sourceElement = document.getElementById(sourceId);

    if (sourceElement.style.maxHeight) {
        sourceElement.style.maxHeight = null;
    } else {
        sourceElement.style.maxHeight = sourceElement.scrollHeight + "px";
    }
}

