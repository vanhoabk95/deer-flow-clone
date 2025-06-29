import { parse } from "best-effort-json-parser";

export function parseJSON<T>(json: string | null | undefined, fallback: T) {
  if (!json) {
    return fallback;
  }
  try {
    const raw = json
      .trim()
      .replace(/^```js\s*/, "")
      .replace(/^```json\s*/, "")
      .replace(/^```ts\s*/, "")
      .replace(/^```plaintext\s*/, "")
      .replace(/^```markdown\s*/, "")
      .replace(/^```\s*/, "")
      .replace(/\s*```$/, "");
    
    // Check if this looks like JSON (starts with [ or {)
    if (!raw.startsWith('[') && !raw.startsWith('{')) {
      console.warn('parseJSON: Input does not look like JSON, returning fallback:', { 
        input: json.substring(0, 100) + (json.length > 100 ? '...' : ''),
        raw: raw.substring(0, 100) + (raw.length > 100 ? '...' : '')
      });
      return fallback;
    }
    
    return parse(raw) as T;
  } catch (error) {
    console.warn('parseJSON: Failed to parse JSON, returning fallback:', { 
      error: error instanceof Error ? error.message : 'Unknown error',
      input: json.substring(0, 100) + (json.length > 100 ? '...' : '')
    });
    return fallback;
  }
}
