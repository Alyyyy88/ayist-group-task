window.addEventListener("load", function () {
  try {
    function simpleCounter(element, target, duration, step) {
      if (!element) return;

      let current = 0;
      const increment = target / ((duration * 1000) / step);
      const timer = setInterval(() => {
        current += increment;
        if (current >= target) {
          current = target;
          clearInterval(timer);
        }

        if (element.classList.contains("currency-count-up")) {
          element.textContent = "$" + Math.floor(current).toLocaleString();
        } else if (element.classList.contains("percent-count-up")) {
          element.textContent = current.toFixed(1) + "%";
        } else if (element.classList.contains("decimal-count-up")) {
          element.textContent = current.toFixed(1);
        } else {
          element.textContent = Math.floor(current);
        }
      }, step);
    }

    // Animate all counter elements
    document
      .querySelectorAll(
        ".count-up, .currency-count-up, .percent-count-up, .decimal-count-up"
      )
      .forEach((el) => {
        const target = parseFloat(el.getAttribute("data-target"));
        simpleCounter(el, target, 2, 30); // 2 seconds duration, update every 30ms
      });

    // Animate storage bar
    const storageBar = document.getElementById("storageBar");
    if (storageBar) {
      let width = 0;
      const maxWidth = 45; // 45%
      const interval = setInterval(() => {
        width += 1;
        if (width > maxWidth) {
          clearInterval(interval);
          width = maxWidth;
        }
        storageBar.style.width = width + "%";
      }, 40); // ~2 seconds to complete
    }

    // Animate cards
    const cards = document.querySelectorAll('[id^="card"]');
    cards.forEach((card, index) => {
      // Set initial state
      card.style.opacity = "0";
      card.style.transform = "translateY(20px)";

      // Animate with setTimeout for sequence
      setTimeout(() => {
        card.style.transition = "opacity 0.5s ease, transform 0.5s ease";
        card.style.opacity = "1";
        card.style.transform = "translateY(0)";
      }, index * 100);
    });
  } catch (e) {
    console.error("Error in animation:", e);
  }

  // Second attempt with GSAP if available
  setTimeout(() => {
    try {
      if (typeof gsap !== "undefined") {
        // Simple entrance animation for cards
        const cards = document.querySelectorAll('[id^="card"]');
        gsap.set(cards, { y: 20, opacity: 0 });

        gsap.to(cards, {
          duration: 0.5,
          y: 0,
          opacity: 1,
          stagger: 0.1,
          ease: "power1.out",
        });

        // Number counters
        document.querySelectorAll(".count-up").forEach((el) => {
          const target = parseInt(el.getAttribute("data-target"));
          gsap.to(el, {
            innerHTML: target,
            duration: 2,
            ease: "power1.out",
            snap: { innerHTML: 1 },
          });
        });

        // Currency counters
        document.querySelectorAll(".currency-count-up").forEach((el) => {
          const target = parseInt(el.getAttribute("data-target"));
          const obj = { val: 0 };
          gsap.to(obj, {
            val: target,
            duration: 2,
            onUpdate: function () {
              el.innerHTML = "zł " + Math.floor(obj.val).toLocaleString();
            },
          });
        });

        // Percentage counters
        document.querySelectorAll(".percent-count-up").forEach((el) => {
          const target = parseFloat(el.getAttribute("data-target"));
          const obj = { val: 0 };
          gsap.to(obj, {
            val: target,
            duration: 2,
            onUpdate: function () {
              el.innerHTML = obj.val.toFixed(1) + "%";
            },
          });
        });

        // Decimal counters
        document.querySelectorAll(".decimal-count-up").forEach((el) => {
          const target = parseFloat(el.getAttribute("data-target"));
          const obj = { val: 0 };
          gsap.to(obj, {
            val: target,
            duration: 2,
            onUpdate: function () {
              el.innerHTML = obj.val.toFixed(1);
            },
          });
        });

        // Storage bar
        const storageBar = document.getElementById("storageBar");
        if (storageBar) {
          gsap.to(storageBar, {
            width: "45%",
            duration: 2,
            ease: "power2.out",
          });
        }
      }
    } catch (e) {
      console.error("Error in GSAP animation:", e);
    }
  }, 500);
});

document.addEventListener("DOMContentLoaded", function () {
  setTimeout(() => {
    const counterElements = document.querySelectorAll(
      ".count-up, .currency-count-up, .percent-count-up, .decimal-count-up"
    );

    counterElements.forEach((el) => {
      el.style.transition = "color 1s ease";
      el.style.color = "#ff0000";

      setTimeout(() => {
        el.style.color = "";
      }, 1000);
    });
  }, 1000);
});
