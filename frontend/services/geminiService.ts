
export const GeminiService = {
  getWelcomeInsight: async (userName: string): Promise<string> => {
    return `Bem-vindo de volta, ${userName}.`;
  },

  suggestCategory: async (_transactionDescription: string): Promise<string> => {
    return "Geral";
  }
};
