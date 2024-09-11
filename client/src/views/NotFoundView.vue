<script setup lang="ts">
import {useRouter} from 'vue-router'
import {ServerCrash} from 'lucide-vue-next'

const router = useRouter()
</script>

<template>
  <div class="h-[90vh] flex items-center justify-center gap-1">
    <ServerCrash /> Not Found
  </div>
</template>
