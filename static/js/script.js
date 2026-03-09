document.addEventListener("DOMContentLoaded", function(){
    updateClock();

    // run client-side search filtering if table exists
    const searchInput = document.getElementById("searchInput");
    if (searchInput) {
        searchInput.addEventListener("keyup", function () {
            let filter = searchInput.value.toLowerCase();
            let rows = document.querySelectorAll("#attendanceTable tr");
            rows.forEach((row, index) => {
                if (index === 0) return; // header
                let text = row.textContent.toLowerCase();
                row.style.display = text.includes(filter) ? "" : "none";
            });
        });
    }
});

function updateClock(){
    const clock = document.getElementById("clock");
    if(clock){
        setInterval(()=>{
            const now = new Date();
            clock.innerHTML = "Current Time: " + now.toLocaleTimeString();
        },1000);
    }
}


/* ================= PARTICLES NETWORK ONLY HOMEPAGE ================= */
if (document.body.classList.contains("home-page")) {
    particlesJS("particles-js", {
        particles: {
            number: { value: 80 },
            color: { value: "#00c3ff" },
            shape: { type: "circle" },
            opacity: { value: 0.5 },
            size: { value: 3 },
            line_linked: {
                enable: true,
                distance: 150,
                color: "#00c3ff"
            },
            move: { enable: true, speed: 2 }
        }
    });
}


/* ================= ATTENDANCE SEARCH (now handled on DOMContentLoaded) ================= */

// logic moved into the DOMContentLoaded handler to ensure elements exist


/* ================= ATTENDANCE CHART ================= */

// chart initialization removed; create your own if needed by
// providing live data and a <canvas id="attendanceChart"> element.
// https://chatgpt.com/s/t_69ae543676808191bd1aa81fbfc77aa1