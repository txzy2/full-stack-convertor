import {defineStore} from 'pinia'

export const useUserStorage = defineStore('user', {
  state: () => ({
    theme: 'dark'
  }),
  actions: {
    setTheme(theme: string) {
      this.theme = theme

      localStorage.setItem('user', this.theme)
    }
  },
  getters: {
    getTheme() {
      const theme = localStorage.getItem('user')
      return theme
    }
  }
})
