import { CommonModule } from '@angular/common';
import { Component, inject } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { finalize } from 'rxjs';
import { RagApiService, AskResponse } from './rag-api.service';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, FormsModule],
  template: `
    <div class="page">
      <div class="container">
        <h1>LangChain RAG Demo</h1>
        <p class="subtitle">
          Index files with FastAPI, then ask grounded questions from Angular.
        </p>

        <div class="panel">
          <button (click)="ingest()" [disabled]="loading">
            {{ loading ? 'Working...' : 'Ingest Documents' }}
          </button>
          <p class="status" *ngIf="statusMessage">{{ statusMessage }}</p>
        </div>

        <div class="panel">
          <label for="question">Ask a question</label>
          <textarea
            id="question"
            [(ngModel)]="question"
            rows="5"
            placeholder="What is this document about?"
          ></textarea>

          <button (click)="ask()" [disabled]="loading || !question.trim()">
            {{ loading ? 'Working...' : 'Ask' }}
          </button>
        </div>

        <div class="panel" *ngIf="response">
          <h2>Answer</h2>
          <p class="answer">{{ response.answer }}</p>

          <h3>Sources</h3>
          <div class="source" *ngFor="let source of response.sources">
            <div><strong>File:</strong> {{ source.source }}</div>
            <div *ngIf="source.page !== null && source.page !== undefined">
              <strong>Page:</strong> {{ source.page }}
            </div>
            <p>{{ source.preview }}</p>
          </div>
        </div>
      </div>
    </div>
  `,
  styles: [
    `
      .page {
        min-height: 100vh;
        padding: 32px 16px;
      }

      .container {
        max-width: 900px;
        margin: 0 auto;
      }

      h1 {
        margin-bottom: 8px;
      }

      .subtitle {
        margin-top: 0;
        color: #4b5563;
      }

      .panel {
        background: white;
        border-radius: 16px;
        padding: 20px;
        margin-top: 20px;
        box-shadow: 0 8px 24px rgba(15, 23, 42, 0.08);
      }

      textarea {
        width: 100%;
        margin: 10px 0 16px;
        padding: 12px;
        border-radius: 12px;
        border: 1px solid #d1d5db;
        resize: vertical;
        font: inherit;
      }

      button {
        background: #2563eb;
        color: white;
        border: none;
        border-radius: 10px;
        padding: 10px 16px;
        cursor: pointer;
        font-weight: 600;
      }

      button:disabled {
        opacity: 0.6;
        cursor: not-allowed;
      }

      .status {
        margin-top: 12px;
      }

      .answer {
        white-space: pre-wrap;
        line-height: 1.6;
      }

      .source {
        border-top: 1px solid #e5e7eb;
        padding-top: 12px;
        margin-top: 12px;
      }
    `
  ]
})
export class AppComponent {
  private readonly api = inject(RagApiService);

  question = '';
  loading = false;
  statusMessage = '';
  response: AskResponse | null = null;

  ingest(): void {
    this.loading = true;
    this.statusMessage = '';

    this.api
      .ingest(true)
      .pipe(finalize(() => (this.loading = false)))
      .subscribe({
        next: (res) => {
          this.statusMessage = `${res.message} Indexed files: ${res.indexed_files}, chunks: ${res.indexed_chunks}.`;
        },
        error: (err) => {
          this.statusMessage = err?.error?.detail ?? 'Failed to ingest documents.';
        }
      });
  }

  ask(): void {
    if (!this.question.trim()) return;

    this.loading = true;
    this.statusMessage = '';

    this.api
      .ask(this.question.trim())
      .pipe(finalize(() => (this.loading = false)))
      .subscribe({
        next: (res) => {
          this.response = res;
        },
        error: (err) => {
          this.statusMessage = err?.error?.detail ?? 'Failed to fetch answer.';
        }
      });
  }
}
