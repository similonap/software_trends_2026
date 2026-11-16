import react, { reactCompilerPreset } from '@vitejs/plugin-react'
import babel from '@rolldown/plugin-babel'
import { defineConfig } from 'vite'

// https://vite.dev/config/
export default defineConfig({
  plugins: [
    react(),
    // Opdracht 1.3: de React Compiler staat aan
    babel({ presets: [reactCompilerPreset()] }),
  ],
})
