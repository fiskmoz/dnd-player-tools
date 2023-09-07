import { defineStore } from 'pinia'
import { Api, type CharacterSheetResponse, type HttpResponse } from 'domain/client'

export const useCharacterStore = defineStore('character', () => {
  function createCharacter(): Promise<HttpResponse<CharacterSheetResponse, any>> {
    return new Api().characterSheets.createCharacterSheetCharacterSheetsPost()
  }

  return {}
})
