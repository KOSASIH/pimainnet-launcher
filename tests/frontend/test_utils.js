import { waitFor } from '@testing-library/react';

describe('waitForElement', () => {
  it('waits for the element to be visible', async () => {
    const element = document.createElement('div');
    element.style.display = 'none';
    document.body.appendChild(element);
    await waitFor(() => element.style.display === 'block');
    expect(element.style.display).toBe('block');
  });

  it('throws an error if the element is not visible after the timeout', async () => {
    const element = document.createElement('div');
    element.style.display = 'none';
    document.body.appendChild(element);
    await expect(waitFor(() => element.style.display === 'block', { timeout: 100 })).rejects.toThrowError(
      'Timed out waiting for element to be visible'
    );
  });
});
