<script lang="ts">
import { Api } from '@/domain/client'
import { defineComponent } from 'vue'

export default defineComponent({
  components: {},
  data() {
    return {
      characterSheet: null
    }
  }
})
</script>

<template>
  <div class="container">
    <div class="col-12">
      <div class="fw-bold">AI Character Creation</div>
    </div>
    <div class="container">
      <div class="col-12">
        <button>Navigate to new</button>
      </div>
    </div>
  </div>
</template>

<style></style>
