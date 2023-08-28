export async function postUrlToFlaskServer(url: string): Promise<any> {
  const response = await fetch('http://your-flask-server-url/api/endpoint', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ url }),
  });

  if (!response.ok) {
    throw new Error('Failed to fetch');
  }

  const data = await response.json();
  return data;
}
