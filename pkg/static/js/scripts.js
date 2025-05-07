

$('documents').ready( ()=>{
    // loading section
    let content = $('#content')
    let loader = $('#spinner')

    setTimeout(()=>{
        loader.css('display', 'none')
        content.css('display', 'block')
        AOS.init()
    },500)

    // visuals effects:
    function hide(id){ $(`#${id}`).fadeOut(400, function() {$(this).css('display', 'none').remove();}); }

    // auto disable acadimicYearSelect If The Value != 'تلميذ' 
    $("#roleSelect").change(()=>{
        const acadimicYearSelect = $('#acadimicYearSelect');
        const isStudent = $('#roleSelect').val() === 'تلميذ'
        acadimicYearSelect.toggleClass('disabled_', !isStudent);
    })
    // admin Page
    
})
    

   