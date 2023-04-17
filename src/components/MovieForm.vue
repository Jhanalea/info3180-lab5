<template>
    <div
        v-if="displayFlash"
        v-bind:class="[isSuccess ? alertSuccessClass : alertErrorClass]"
        class="alert">
        {{ flashMessage }}
    </div>

  <form ref="movieForm" @submit.prevent="saveMovie" method="post" enctype="multipart/form-data" id="movieForm">

    <div class="form-group mb-3">
      <label for="title" class="form-label">Movie Title</label>
      <input type="text" name="title" id="title" class="form-control" required>
    </div>

    <div class="form-group mb-3">
      <label for="description" class="form-label">Movie Description</label>
      <textarea name="description" id="description" class="form-control" required></textarea>
    </div>

    <div class="form-group mb-3">
      <label for="poster" class="form-label">Movie Poster</label>
      <input type="file" name="poster" id="poster" class="form-control" accept="image/*" required />
    </div>

    <button type="submit" class="btn btn-primary">Save Movie</button>

  </form>
</template>

<script setup>
import { ref, onMounted } from "vue";

let csrf_token = ref("");
let flashMessage = ref("");
let displayFlash = ref(false);
let isSuccess = ref(false);
let alertSuccessClass = ref("alert-success");
let alertErrorClass = ref("alert-danger");

// Define refs for form fields
let title = ref("");
let description = ref("");
let poster = ref("");


onMounted(getCsrfToken);

function getCsrfToken() {
        fetch('/api/v1/csrf-token')
        .then((response) => response.json())
        .then((data) => {
            console.log(data);
            csrf_token.value = data.csrf_token;
        })
    }

function clearFormFields() {
  title.value = "";
  description.value = "";
  poster.value = "";
}

async function saveMovie() {
  let movieForm = document.getElementById("movieForm");
  let form_data = new FormData(movieForm);

  try {
    let response = await fetch("/api/v1/movies", {
      method: 'POST',
      body: form_data,
      headers: {
        'X-CSRFToken': csrf_token.value
      }
    });
    let data = await response.json();

    if ("errors" in data) {
      flashMessage.value = [...data.errors];
      isSuccess.value = false;
      displayFlash.value = true;
    }
    else {
      isSuccess.value = true;
      flashMessage.value = "Movie Added Successfully!";
      displayFlash.value = true;
      clearFormFields();

    }
  }
  catch (error) {
    console.log(error);
  }
}
</script>
