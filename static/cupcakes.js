const API_URL = "http://localhost:5000/api";

/** generate HTML for a cupcake */
function cupcakeHTML(cupcake) {
  return `
    <div data-cupcake-id=${cupcake.id}>
      <li>${cupcake.flavor} (${cupcake.size}) - Rating: ${cupcake.rating}</li>
      <button class="delete-btn">Remove</button>
      <img src="${cupcake.image}" alt="${cupcake.flavor} cupcake" class="cupcake-img">
    </div>
  `;
}

/** show initial cupcakes on page */
async function loadCupcakes() {
  const response = await axios.get(`${API_URL}/cupcakes`);
  const cupcakesList = response.data.cupcakes;

  for (let cupcake of cupcakesList) {
    $("#cupcakes-list").append(cupcakeHTML(cupcake));
  }
}

/** handle submission of new cupcake form */
$("#new-cupcake-form").on("submit", async function (event) {
  event.preventDefault();

  const flavor = $("#form-flavor").val(); 
  const size = $("#form-size").val().toLowerCase(); // Convert to lowercase
  const rating = $("#form-rating").val(); 
  const image = $("#form-image").val() || null; 

  const response = await axios.post(`${API_URL}/cupcakes`, {
    flavor, size, rating, image
  });

  const newCupcake = response.data.cupcake;
  $("#cupcakes-list").append(cupcakeHTML(newCupcake));
  $("#new-cupcake-form").trigger("reset");
});

/** handle clicking delete button to remove a cupcake */
$("#cupcakes-list").on("click", ".delete-btn", async function (evt) {
  evt.preventDefault();

  const $cupcakeDiv = $(evt.target).closest("div");
  const cupcakeId = $cupcakeDiv.data("cupcake-id");

  // Send DELETE request to API to remove cupcake
  await axios.delete(`${API_URL}/cupcakes/${cupcakeId}`);

  // Remove the cupcake element from the DOM
  $cupcakeDiv.remove();
});

$(loadCupcakes);
