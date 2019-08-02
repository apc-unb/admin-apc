function filter_period(el) {
    const element = document.getElementById(el);
    const value = element.options[element.selectedIndex].value;
    const periods = classes.filter( (c, idx) => {
        return c.year == value;
    }).map((e, idx) => {
        return e.season;
    });
    const select_element = document.getElementById('filtra-periodo-listar');
    for (i = 0; i < select_element.options.length; i++){
        if(!periods.includes(Number(select_element.options[i].value))){
            console.log("Disabling option", select_element.options[i]);
            select_element.options[i].disabled = true;
        } else {
            select_element.options[i].disabled = false;
        }
    }
}