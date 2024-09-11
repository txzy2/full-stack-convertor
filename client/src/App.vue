<script setup lang="ts">
import {ref, onMounted, watch} from 'vue'
import {RouterLink, RouterView, useRoute} from 'vue-router'
import {Motion} from '@oku-ui/motion'
import axios from 'axios'
import {ServerCrash} from 'lucide-vue-next'

import {Header} from '@/components/'
import {Loader} from '@/components/ui/loader'

import {
  Breadcrumb,
  BreadcrumbItem,
  BreadcrumbLink,
  BreadcrumbList,
  BreadcrumbPage,
  BreadcrumbSeparator
} from '@/components/ui/breadcrumb'

const loader = ref<boolean>(true)
const error = ref<string>('')

const breadcrumbs = ref<Array<{name: string; path: string}>>([])

onMounted(() => {
  const res = axios.get('http://127.0.0.1:8000/').then(res => {
    if (res.status === 200) {
      loader.value = false
    }
  })

  res.catch(err => {
    error.value = 'Server Error'
  })
})

const route = useRoute()

const generateBreadcrumbs = () => {
  const pathArray = route.path.split('/').filter(p => p)
  const breadcrumbArray: any[] = pathArray.map((path, index) => {
    const fullPath = '/' + pathArray.slice(0, index + 1).join('/')
    const routeMatch = route.matched.find(r => r.path === fullPath)
    return {
      name: routeMatch?.name || path,
      path: fullPath
    }
  })

  breadcrumbs.value = [{name: 'Home', path: '/'}, ...breadcrumbArray]
}

watch(route, generateBreadcrumbs, {immediate: true})
</script>

<template>
  <Header />

  <Breadcrumb
    v-show="route.name !== 'NotFound' && !loader"
    class="h-[3vh] flex justify-center"
  >
    <BreadcrumbList>
      <BreadcrumbItem v-for="(breadcrumb, index) in breadcrumbs" :key="index">
        <template v-if="breadcrumb.path === $route.path">
          <BreadcrumbPage class="font-semibold">
            {{ breadcrumb.name }}
          </BreadcrumbPage>
        </template>
        <template v-else>
          <BreadcrumbLink>
            <RouterLink :to="breadcrumb.path">
              {{ breadcrumb.name }}
            </RouterLink>
          </BreadcrumbLink>
        </template>
        <BreadcrumbSeparator v-if="index < breadcrumbs.length - 1" />
      </BreadcrumbItem>
    </BreadcrumbList>
  </Breadcrumb>

  <Loader
    v-if="loader"
    :size="30"
    :error="error"
    :sub="{need: true, text: 'Configuring Server', size: 15}"
  />

  <Motion
    v-else
    :initial="{opacity: 0, scale: 0}"
    :animate="{opacity: 1, scale: 1}"
    :exit="{opacity: 0, scale: 0.3}"
  >
    <RouterView />
  </Motion>

  <!-- TODO: Сделать футер с статистикой конвертаций -->
</template>
