import React, { useState } from 'react';
import axios from 'axios';
import { QueryForm } from './components/QueryForm';
import { CodeOutput } from './components/CodeOutput';
import { LoadingState } from './components/LoadingState';

interface CodeResponse {
  code: string;
  explanation: string;
  language: string;
  complexity: string;
  agents_used: string[];
  processing_time: number;
}

const AGENTS = [
  'Orchestrator',
  'Frontend Dev',
  'Backend Dev',
  'Testing',
  'Documentation'
];

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

function App() {
  const [result, setResult] = useState<CodeResponse | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [currentAgent, setCurrentAgent] = useState('Orchestrator');

  const handleSubmit = async (
    query: string,
    context: string,
    language: string
  ) => {
    setLoading(true);
    setError(null);
    setResult(null);
    
    try {
      // Simulate agent processing
      const agentSequence = AGENTS;
      for (const agent of agentSequence) {
        setCurrentAgent(agent);
        await new Promise(resolve => setTimeout(resolve, 500));
      }

      const response = await axios.post(
        `${API_URL}/api/process-query`,
        {
          query,
          context: context || undefined,
          language,
        }
      );

      // The backend returns QueryResponse with nested data structure
      const resultData = response.data.data;
      const fullResult = {
        ...resultData,
        agents_used: response.data.agents_involved || AGENTS,
        processing_time: response.data.processing_time_ms || 0
      };
      
      setResult(fullResult);
    } catch (err) {
      const message = axios.isAxiosError(err)
        ? err.response?.data?.detail || 'Failed to generate code'
        : 'An unexpected error occurred';
      setError(message);
      console.error('Error:', err);
    } finally {
      setLoading(false);
      setCurrentAgent('Orchestrator');
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-purple-900 to-slate-900">
      {/* Header */}
      <header className="bg-black/40 backdrop-blur-md border-b border-purple-500/20 sticky top-0 z-50">
        <div className="max-w-6xl mx-auto px-4 py-6">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-3">
              <div className="w-10 h-10 bg-gradient-to-br from-blue-400 to-purple-500 rounded-lg flex items-center justify-center">
                <span className="text-white font-bold text-lg">⚙️</span>
              </div>
              <div>
                <h1 className="text-2xl font-bold text-white">AutoCoder Agents</h1>
                <p className="text-sm text-purple-200">AI-Powered Code Generation</p>
              </div>
            </div>
            <a
              href="https://github.com"
              target="_blank"
              rel="noopener noreferrer"
              className="px-4 py-2 rounded-lg bg-purple-600/20 border border-purple-500/30 text-purple-200 hover:bg-purple-600/40 transition"
            >
              GitHub
            </a>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="max-w-6xl mx-auto px-4 py-12">
        <div className="space-y-8">
          {/* Status Message */}
          {error && (
            <div className="p-4 bg-red-900/20 border border-red-500/30 rounded-lg text-red-200">
              <p className="font-semibold">Error</p>
              <p className="text-sm mt-1">{error}</p>
            </div>
          )}

          {/* Form Section */}
          <div className="space-y-4">
            <h2 className="text-lg font-semibold text-white">Describe Your Code Idea</h2>
            <QueryForm onSubmit={handleSubmit} isLoading={loading} />
          </div>

          {/* Loading State */}
          {loading && (
            <div className="space-y-4">
              <h2 className="text-lg font-semibold text-white">Processing</h2>
              <LoadingState agents={AGENTS} currentAgent={currentAgent} />
            </div>
          )}

          {/* Results Section */}
          {result && !loading && (
            <div className="space-y-4">
              <h2 className="text-lg font-semibold text-white">Generated Code</h2>
              <CodeOutput
                code={result.code}
                explanation={result.explanation}
                language={result.language}
                complexity={result.complexity}
              />
              <div className="p-4 bg-slate-800/50 rounded-lg border border-purple-500/20">
                <p className="text-sm text-gray-300">
                  <span className="font-semibold text-purple-300">Processing Time:</span> {result.processing_time.toFixed(2)}ms
                </p>
                <p className="text-sm text-gray-300 mt-2">
                  <span className="font-semibold text-purple-300">Agents Used:</span> {result.agents_used.join(', ')}
                </p>
              </div>
            </div>
          )}

          {/* Empty State */}
          {!result && !loading && (
            <div className="text-center py-12">
              <p className="text-gray-400">
                Enter your code requirements above to get started.
              </p>
            </div>
          )}
        </div>
      </main>

      {/* Footer */}
      <footer className="border-t border-purple-500/20 bg-black/20 mt-12">
        <div className="max-w-6xl mx-auto px-4 py-6 text-center text-sm text-gray-400">
          <p>AutoCoder Agents © 2024 | Built with React, FastAPI, and AI</p>
        </div>
      </footer>
    </div>
  );
}

export default App;
