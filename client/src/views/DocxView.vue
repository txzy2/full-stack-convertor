<script setup lang="ts">
import {ref} from 'vue'
import {useRouter} from 'vue-router'
import axios from 'axios'
import {ArrowRightToLine, Download, RefreshCcw, House} from 'lucide-vue-next'

import confetti from 'canvas-confetti'

import {Button} from '@/components/ui/button'
import {Badge} from '@/components/ui/badge'
import {Loader} from '@/components/ui/loader'

const router = useRouter()
const fileStatus = ref<boolean>(false)
const loading = ref<boolean>(false)

const file = ref<File | null>()
const form = ref<HTMLFormElement>()

const url = ref<string>('')
const fileName = ref<string>('')
const success = ref<boolean>(false)

const onChange = ($event: Event) => {
  const target = $event.target as HTMLInputElement

  if (target && target.files) {
    file.value = target.files[0]

    fileName.value = file.value.name
    fileStatus.value = true

    console.log(fileName.value, fileStatus.value)
  }
}

const triggerFileInput = () => {
  const input = document.getElementById('fileInput') as HTMLInputElement
  if (input) {
    input.click()
  }
}

const restart = () => {
  file.value = null
  fileName.value = ''
  fileStatus.value = false
  url.value = ''
  success.value = false
}

const pushFile = async () => {
  if (file.value) {
    loading.value = true

    const formData = new FormData()
    formData.append('file', file.value)

    const response = await axios.post(
      'http://127.0.0.1:8000/docxtopdf',
      formData,
      {
        headers: {
          'Content-Type': 'multipart/form-data'
        },
        responseType: 'blob'
      }
    )

    if (response.status === 200) {
      url.value = URL.createObjectURL(response.data)

      loading.value = false
      success.value = true

      fileName.value = `${file.value.name.replace('.docx', '')}.pdf`
    }
  }
}
</script>

<template>
  <div class="h-[87vh] flex flex-col items-center justify-center gap-3">
    <div class="flex items-center gap-2">
      <p class="rounded-sm text-[15px]">Docx(Doc) -> PDF</p>

      <form id="addForm" ref="form" @submit.prevent="pushFile">
        <Button
          v-show="!fileStatus"
          type="button"
          class="h-[30px]"
          @click="triggerFileInput"
        >
          Add File
        </Button>

        <input
          id="fileInput"
          type="file"
          accept=".docx"
          class="hidden"
          @change="onChange"
        />
      </form>

      <Badge
        variant="outline"
        v-show="fileStatus"
        class="h-[30px] rounded-sm"
        >{{ fileName }}</Badge
      >

      <Button
        v-show="fileStatus && !loading && !success"
        form="addForm"
        type="submit"
        title="Convert"
        class="h-[30px] flex items-center gap-1"
      >
        <ArrowRightToLine />
      </Button>

      <Badge
        v-show="success"
        variant="outline"
        class="h-[30px] rounded-sm transition-all duration-300 hover:scale-110"
      >
        <a
          :href="url"
          v-show="success"
          :download="fileName"
          @click="
            () => {
              confetti({
                particleCount: 80,
                spread: 90,
                origin: {y: 0.8}
              })
            }
          "
        >
          <Download :size="18" />
        </a>
      </Badge>
    </div>

    <Loader
      v-show="loading"
      :size="20"
      :height="5"
      :sub="{text: 'Converting...', need: true, size: 14}"
    />

    <div v-show="file" class="flex items-center gap-1">
      <div class="group leading-none">
        <Button
          v-show="success"
          variant="outline"
          class="h-[30px]"
          @click="restart"
        >
          <RefreshCcw class="group-hover:animate-spin" />
        </Button>
      </div>

      <Button variant="outline" class="h-[30px]" @click="router.push('/')">
        <House />
      </Button>
    </div>
  </div>
</template>
