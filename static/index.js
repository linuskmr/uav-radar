function render_drone(drone_id, drone) {
    const coordinate_scale = 9
    let dom_drone = document.getElementById(`drone_${drone_id}`)
    let drone_x = drone['position']['latitude'] * coordinate_scale
    let drone_y = drone['position']['longitude'] * coordinate_scale

    const drone_icon = `<svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-drone" width="30" height="30" viewBox="0 0 24 24" stroke-width="1.5" stroke="#2c3e50" fill="none" stroke-linecap="round" stroke-linejoin="round">
      <path stroke="none" d="M0 0h24v24H0z" fill="none"/>
      <path d="M10 10h4v4h-4z" />
      <line x1="10" y1="10" x2="6.5" y2="6.5" />
      <path d="M9.96 6a3.5 3.5 0 1 0 -3.96 3.96" />
      <path d="M14 10l3.5 -3.5" />
      <path d="M18 9.96a3.5 3.5 0 1 0 -3.96 -3.96" />
      <line x1="14" y1="14" x2="17.5" y2="17.5" />
      <path d="M14.04 18a3.5 3.5 0 1 0 3.96 -3.96" />
      <line x1="10" y1="14" x2="6.5" y2="17.5" />
      <path d="M6 14.04a3.5 3.5 0 1 0 3.96 3.96" />
    </svg>`

    if (dom_drone == null) {
        document.getElementById('content').innerHTML += `
            <div id="drone_${drone_id}" style="position: absolute; top: ${drone_x}px; left: ${drone_y}px; transition: all 1s;">
                <a href="info/${drone_id}">${drone_icon}</a>
            </div>`
    } else {
        dom_drone.style.top = `${drone_x}px`
        dom_drone.style.left =`${drone_y}px`
    }
}

function load_data() {
    fetch('api/flight_map')
        .then(response => response.json())
        .then(data => {
            for (const [drone_id, drone] of Object.entries(data)) {
                render_drone(drone_id, drone)
            }
        })
}

function sse() {
    console.log('eventsource')
    let event_src = new EventSource('/stream');
    event_src.onmessage = function (e) {
        const drone = JSON.parse(e.data)
        render_drone(drone['id'], drone)
    }
}
load_data()
sse()