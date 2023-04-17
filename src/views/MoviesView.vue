<template>
    <div class="movies">
        <div v-for="movie in movies" :key="movie.id" class="movie-card">
            <div class="movie-image-container">
                <img :src="movie.poster" class="movie-image"  alt="Movie Poster"/>
            </div>
            <div class="movie-info">
                <h3 class="movie-title">{{ movie.title }}</h3>
                <p class="movie-description">{{ movie.description }}</p>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from "vue";


let movies = ref([]);
  async function fetchMovies() {
      let response = await fetch('/api/v1/movies');
      let data = await response.json();
      movies.value = data.data;
  }

  onMounted(() => {
    fetchMovies();
  });

</script>

<style scoped>

.movies {
  display: flex;
  flex-wrap: wrap;
}

.movie-card {
  display: flex;
  background-color: #fff;
  border-radius: 10px;
  box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1);
  margin: 1rem;
  overflow: hidden;
  width: 30%;
}

.movie-image-container {
  width: 40%;
  overflow: hidden;
}

.movie-image {
  width: 100%;
  border-radius: 10px 0 0 10px;
}

.movie-info {
  padding: 1rem;
  width: 60%;
}

.movie-title {
  font-size: 1.5rem;
  margin-bottom: 0.5rem;
}

.movie-description {
  font-size: 1rem;
}
</style>