import React, { useState } from 'react';
import { Send } from 'lucide-react';

interface QueryFormProps {
  onSubmit: (query: string, context: string, language: string) => void;
  isLoading: boolean;
}

export const QueryForm: React.FC<QueryFormProps> = ({ onSubmit, isLoading }) => {
  const [query, setQuery] = useState('');
  const [context, setContext] = useState('');
  const [language, setLanguage] = useState('python');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (query.trim()) {
      onSubmit(query, context, language);
    }
  };

  const exampleQueries = [
    "Build a React login form with email and password",
    "Create a Python function to reverse a string",
    "Write a REST API endpoint for user management",
  ];

  return (
    <div className="w-full max-w-2xl mx-auto p-6 bg-white rounded-lg shadow-lg">
      <form onSubmit={handleSubmit} className="space-y-4">
        <div>
          <label className="block text-sm font-semibold text-gray-700 mb-2">
            What would you like me to code?
          </label>
          <textarea
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            placeholder="e.g., Build a React login form..."
            className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent resize-none"
            rows={4}
            disabled={isLoading}
          />
          <p className="text-xs text-gray-500 mt-1">Be as specific as possible</p>
        </div>

        <div>
          <p className="text-xs text-gray-600 mb-2">Quick examples:</p>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-2">
            {exampleQueries.map((example, idx) => (
              <button
                key={idx}
                type="button"
                onClick={() => setQuery(example)}
                className="text-left text-xs p-2 bg-gray-100 hover:bg-gray-200 rounded transition"
                disabled={isLoading}
              >
                {example}
              </button>
            ))}
          </div>
        </div>

        <div>
          <label className="block text-sm font-semibold text-gray-700 mb-2">
            Context (optional)
          </label>
          <input
            type="text"
            value={context}
            onChange={(e) => setContext(e.target.value)}
            placeholder="e.g., Using TypeScript, target React 18"
            className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
            disabled={isLoading}
          />
        </div>

        <div>
          <label className="block text-sm font-semibold text-gray-700 mb-2">
            Preferred Language
          </label>
          <select
            value={language}
            onChange={(e) => setLanguage(e.target.value)}
            className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
            disabled={isLoading}
          >
            <option value="python">Python</option>
            <option value="javascript">JavaScript</option>
            <option value="typescript">TypeScript</option>
            <option value="java">Java</option>
            <option value="cpp">C++</option>
            <option value="go">Go</option>
          </select>
        </div>

        <button
          type="submit"
          disabled={isLoading || !query.trim()}
          className="w-full bg-blue-600 hover:bg-blue-700 disabled:bg-gray-400 text-white font-semibold py-3 rounded-lg flex items-center justify-center gap-2 transition"
        >
          <Send size={20} />
          {isLoading ? 'Agents Working...' : 'Generate Code'}
        </button>
      </form>
    </div>
  );
};
