function CallMessage(message,color="danger"){
    // style dict
    const style = {
        'danger': 'bg-danger text-white',
        'success': 'bg-success text-white',
        'waiting': 'bg-warning text-white',
    }
    // Remove style values
    $('#errorMessage').removeClass( Object.values(style).join(' ') );

    // Change color based on the 'color' parameter
    $('#errorMessage').addClass(style[color]);

    const messageDiv = document.getElementById('errorMessage');
    messageDiv.textContent = message;
    $('.toast').toast({ delay: 1500 });
    $('.toast').toast('show');
}