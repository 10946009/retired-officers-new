window.addEventListener('DOMContentLoaded', event => {
    // Simple-DataTables
    // https://github.com/fiduswriter/Simple-DataTables/wiki
    
    const datatablesSimple = document.getElementById('datatablesSimple');
    let options = {
        info: false,
        paging: false,
        searchable: true, // Default to true
    };

    // Check if the datatablesSimple element has a 'search' attribute
    if (datatablesSimple && datatablesSimple.getAttribute('search') === 'false') {
        options.searchable = false;
    }

    if (datatablesSimple) {
        new simpleDatatables.DataTable(datatablesSimple, options);
    }
});
