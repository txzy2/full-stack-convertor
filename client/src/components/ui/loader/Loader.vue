<script setup lang="ts">
import {Loader, Settings, ServerCrash} from 'lucide-vue-next'
import {Motion} from '@oku-ui/motion'

import type {LoaderProps} from '@/types/types'

const props = withDefaults(defineProps<LoaderProps>(), {
  size: 20,
  height: 90,
  error: ''
})
</script>

<template>
  <div :class="`h-[${props.height}vh] flex items-center justify-center gap-2`">
    <Settings v-if="!props.error" class="animate-spin" :size="props.size" />

    <Motion
      v-show="!props.error"
      :initial="{opacity: 0, scale: 0}"
      :animate="{opacity: 1, scale: 1}"
      :exit="{opacity: 0, scale: 0.3}"
    >
      <p v-if="props.sub?.need" :style="{fontSize: `${props.sub?.size}px`}">
        {{ props.sub?.text }}
      </p>
    </Motion>

    <p v-show="props.error" class="flex items-center gap-1">
      <ServerCrash :size="props.size" /> {{ props.error }} :(
    </p>
  </div>
</template>
