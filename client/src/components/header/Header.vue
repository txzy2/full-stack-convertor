<script setup lang="ts">
import {useRouter} from 'vue-router'
import {ServerCog} from 'lucide-vue-next'

import {Button} from '@/components/ui/button'
import {ThemeSwitcher} from '@/components/ui/theme'

const router = useRouter()
</script>

<template>
  <header class="h-[10vh] flex items-center justify-between px-20">
    <Button
      variant="ghost"
      class="flex items-center gap-1 p-0 text-[16px] transition-all duration-300 hover:scale-110 hover:bg-transparent"
      @click="$router.push('/')"
    >
      <ServerCog /> ConverT
    </Button>

    <ThemeSwitcher />
  </header>
</template>
