zoom = %%zoom%%
page_where_to_inject = %%page_where_to_inject%%
prototype = %%prototype%%

container = "#page-container"

prototype = prototype.replace('width="800"', 'width="98%"')
prototype = prototype.replace('height="450"', 'height="100%"')

jq = $
slides = pages = $(container).children()
slide = 0

selector = `${container} > div`
$.each($(selector), function(i, el){el.setAttribute("style","margin: 0")})
$(container)[0].setAttribute("style", `zoom: ${zoom}; overflow: hidden`)
$("body")[0].setAttribute("style", "margin: 0")

function goto(newslide) {
    window.location.href = "#" + $(slides[newslide]).attr("id");
    slide = newslide
}

$("html")[0].onkeydown = function(e) {
    console.log(e.code)
    if (e.code === "ArrowRight") {
        goto(slide + 1)
    } else if (e.code === "ArrowLeft") {
        goto(slide - 1)
    }
}

prototype = $(prototype)
prototype.attr("id", "prototype")
prototype.insertAfter(slides[page_where_to_inject])
slides.splice(page_where_to_inject, 0, prototype)
