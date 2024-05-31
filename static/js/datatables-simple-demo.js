window.addEventListener('DOMContentLoaded', event => {
    // Simple-DataTables
    // https://github.com/fiduswriter/Simple-DataTables/wiki
    
    const datatablesSimple = document.getElementById('datatablesSimple');
    let options = {
        info: false,
        paging: false,
        searchable: true,
        
    };
    if (datatablesSimple) {
        new simpleDatatables.DataTable(datatablesSimple,options);

    }
});
