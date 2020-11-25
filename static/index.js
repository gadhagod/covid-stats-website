function go_to_state(){
    var state = document.getElementById('state').value;
    document.write('Loading..')
    window.location.replace('/state/' + state);
}