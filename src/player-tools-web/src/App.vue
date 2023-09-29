<script setup lang="ts"></script>

<template>
  <header>
    <div class="wrapper">
      <HelloWorld msg="You did it!" />

      <nav>
        <RouterLink to="/home">Home</RouterLink>
      </nav>
    </div>
    <div>
      Hej detta är en router view
      <RouterView></RouterView>
    </div>
  </header>
</template>
