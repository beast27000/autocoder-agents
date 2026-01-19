import React from 'react';
import { Copy, Check } from 'lucide-react';
import SyntaxHighlighter from 'react-syntax-highlighter';
import { atomOneDark } from 'react-syntax-highlighter/dist/esm/styles/hljs';

interface CodeOutputProps {
  code: string;
  explanation: string;
  language: string;
  complexity: string;
}

export const CodeOutput: React.FC<CodeOutputProps> = ({ code, explanation, language, complexity }) => {
  const [copied, setCopied] = React.useState(false);

  const handleCopy = () => {
    navigator.clipboard.writeText(code);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  return (
    <div className="w-full max-w-4xl mx-auto mt-8 space-y-6">
      <div className="bg-blue-50 border-l-4 border-blue-500 p-4 rounded">
        <h3 className="font-semibold text-gray-800 mb-2">Explanation</h3>
        <p className="text-gray-700 text-sm">{explanation}</p>
        <div className="flex gap-4 mt-3 text-xs text-gray-600">
          <span>📊 Complexity: {complexity}</span>
          <span>💻 Language: {language.toUpperCase()}</span>
        </div>
      </div>

      <div className="bg-gray-900 rounded-lg overflow-hidden shadow-lg">
        <div className="flex items-center justify-between bg-gray-800 px-4 py-3">
          <span className="text-xs font-mono text-gray-300">CODE OUTPUT</span>
          <button
            onClick={handleCopy}
            className="flex items-center gap-2 px-3 py-1 bg-gray-700 hover:bg-gray-600 rounded text-xs text-gray-200 transition"
          >
            {copied ? (
              <>
                <Check size={16} /> Copied!
              </>
            ) : (
              <>
                <Copy size={16} /> Copy
              </>
            )}
          </button>
        </div>
        <div className="overflow-x-auto">
          <SyntaxHighlighter
            language={language}
            style={atomOneDark}
            customStyle={{ margin: 0, borderRadius: 0 }}
          >
            {code}
          </SyntaxHighlighter>
        </div>
      </div>
    </div>
  );
};
