<script setup lang="ts">
import {Button} from '@/components/ui/button'
import {useRouter} from 'vue-router'

const router = useRouter()
</script>

<template>
  <main class="h-[87vh] flex flex-col items-center justify-center gap-1">
    <h1 class="text-xl">ConverT</h1>

    <div class="flex flex-col items-center gap-1">
      <div class="flex items-center gap-2">
        <Button class="h-[30px]" @click="router.push('/docx')"
          >Docx -> PDF</Button
        >
        <Button class="h-[30px]" @click="router.push('/pdf')"
          >PDF -> Docx</Button
        >
      </div>
    </div>
  </main>
</template>
