<script setup lang="ts">
import {ref, onMounted} from 'vue'
import {Switch} from '@/components/ui/switch'
import {useUserStorage} from '@/stores/storage'

const userStorage = useUserStorage()
const switcher = ref<string | null>(userStorage.getTheme || 'dark')

const active = ref<boolean>(false)

const updateTheme = (theme: string) => {
  document.body.classList.toggle('dark', theme === 'dark')
  active.value = theme === 'dark'
}

const toggle = () => {
  switcher.value = switcher.value === 'dark' ? 'light' : 'dark'
  updateTheme(switcher.value)
  userStorage.setTheme(switcher.value)
}

onMounted(() => {
  updateTheme(switcher.value || 'dark')
})
</script>

<template>
  <Switch
    class="transition-all duration-300 hover:scale-105"
    :checked="active"
    @click="toggle"
  />
</template>
