document.addEventListener("DOMContentLoaded", () => {
  const calcLine = row => {
    const qty  = parseFloat(row.querySelector(".qty-input").value)  || 0;
    const cost = parseFloat(row.querySelector(".cost-input").value) || 0;
    row.querySelector(".line-subtotal").textContent = (qty * cost).toFixed(2);
  };

  const refreshTotal = () => {
    let total = 0;
    document.querySelectorAll(".line-subtotal").forEach(td => {
      total += parseFloat(td.textContent) || 0;
    });
    document.getElementById("grandTotal").textContent = total.toFixed(2);
  };

  /* ——— change events ——— */
  document.body.addEventListener("change", e => {
    const row = e.target.closest("tr");
    if (e.target.matches(".product-select")) {
      /* ixtiyoriy: productdagi data-cost ni cost-input ga qo‘yish  */
      const cost = e.target.selectedOptions[0].dataset.cost || "";
      row.querySelector(".cost-input").value = cost;
      calcLine(row); refreshTotal();
    }
    if (e.target.matches(".qty-input, .cost-input")) {
      calcLine(row); refreshTotal();
    }
  });

  /* ——— add / remove row ——— */
  document.body.addEventListener("click", e => {
    if (e.target.closest(".add-row")) {
      const proto = document.querySelector(".proto");
      const clone = proto.cloneNode(true);
      clone.classList.remove("d-none", "proto");

      const totalForms = document.getElementById("id_form-TOTAL_FORMS");
      const idx = parseInt(totalForms.value, 10);
      clone.innerHTML = clone.innerHTML.replace(/__prefix__/g, idx);
      totalForms.value = idx + 1;

      proto.parentNode.appendChild(clone);
    }

    if (e.target.closest(".remove-row")) {
      const row = e.target.closest("tr");
      row.remove();
      refreshTotal();
    }
  });
});