import { defineStore } from 'pinia'
import { Api } from '@/domain/client'

export const characterSheetStore = defineStore('character', () => {
  function createCharacter(
    request: CharacterSheetRequest
  ): Promise<HttpResponse<CharacterSheetResponse, any>> {
    return new Api().characterSheets.createCharacterSheetCharacterSheetsPost(request)
  }

  return {}
})
