document.addEventListener('DOMContentLoaded', ()=>{
    let content = document.getElementById('content')
    let loader = document.getElementById('spinner')

    setTimeout(()=>{
        loader.style.display = 'none'
        content.style.display = 'block'
    
        AOS.init()
    },0)



    // chat commands
    
})
