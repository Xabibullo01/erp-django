document.addEventListener("DOMContentLoaded", () => {
  const calcLine = row => {
    const qty   = parseFloat(row.querySelector(".qty-input").value)   || 0;
    const price = parseFloat(row.querySelector(".price-input").value) || 0;
    row.querySelector(".line-subtotal").textContent = (qty * price).toFixed(2);   // << Shu yerga diqqat
  };

  const refreshTotal = () => {
    let total = 0;
    document.querySelectorAll(".line-subtotal").forEach(td => {       // << Shu yerga diqqat
      total += parseFloat(td.textContent) || 0;
    });
    document.getElementById("grandTotal").textContent = total.toFixed(2);
  };

  document.body.addEventListener("change", e => {
    // mahsulot tanlandi → narxni qo‘yish
    if (e.target.matches(".product-select")) {
      const price = e.target.selectedOptions[0].dataset.price || 0;
      const row   = e.target.closest("tr");
      row.querySelector(".price-input").value = price;
      calcLine(row);
      refreshTotal();
    }
    // miqdor o‘zgardi
    if (e.target.matches(".qty-input")) {
      const row = e.target.closest("tr");
      calcLine(row);
      refreshTotal();
    }
  });

  // Har safar sahifa yuklanganda barcha qatorlarni hisoblab chiqamiz
  document.querySelectorAll("tr.order-line").forEach(row => {
    calcLine(row);
  });
  refreshTotal();
});