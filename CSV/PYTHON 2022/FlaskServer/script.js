const API = "http://127.0.0.1:81/"
let manaZina = document.querySelector('.manaZina')
let chataZinas = document.querySelector('.chataZinas')
let vards = document.querySelector('.vards')

function suitZinu(){
    console.log("sutitzinu() darbojas")
    chataZinas.innerHTML += '<br/>' + manaZina.Value
    fetch(API+'/sutit/'+vards.value+'/'+manaZina.Value)
}